# Generated by Django 2.0.2 on 2019-03-30 14:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='goods',
            field=models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='goods_num',
            field=models.IntegerField(default=0, help_text='商品数量', verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(help_text='订单信息', on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='trade.OrderInfo', verbose_name='订单信息'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='address',
            field=models.CharField(default='', help_text='收货地址', max_length=100, verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='nonce_str',
            field=models.CharField(blank=True, help_text='随机加密串', max_length=50, null=True, unique=True, verbose_name='随机加密串'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_sn',
            field=models.CharField(blank=True, help_text='订单编号', max_length=30, null=True, unique=True, verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('TRADE_SUCCESS', '成功'), ('TRADE_CLOSED', '超时关闭'), ('WAIT_BUYER_PAY', '交易创建'), ('TRADE_FINISHED', '交易结束'), ('paying', '待支付')], default='paying', help_text='订单状态', max_length=10, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_time',
            field=models.DateTimeField(blank=True, help_text='支付时间', null=True, verbose_name='支付时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_type',
            field=models.CharField(choices=[('alipay', '支付宝'), ('wechat', '微信')], default='alipay', help_text='支付类型', max_length=10, verbose_name='支付类型'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='post_script',
            field=models.FloatField(default=0.0, help_text='订单金额', verbose_name='订单金额'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='signer_mobile',
            field=models.CharField(help_text='联系电话', max_length=11, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='signer_name',
            field=models.CharField(default='', help_text='签收人', max_length=20, verbose_name='签收人'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='trade_no',
            field=models.CharField(blank=True, help_text='交易号', max_length=100, null=True, unique=True, verbose_name='交易号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='goods',
            field=models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='nums',
            field=models.IntegerField(default=0, help_text='购买数量', verbose_name='购买数量'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
